<template>
    <div class="flex flex-col">
		<div v-if="isLoading" class="flex flex-col gap-5">
			<ThreadCard :threadDetails="threadDetails" />

			<CommentCard
                v-if="$store.state.auth.isAuthenticated"
                :username="threadDetails.username"
            />

            <CommentItem
                v-for="(co, index) in $store.state.commentsList"
                :key="index"
                :co="co"
            />
		</div>

        <div v-else 
        class="flex items-center font-semibold text-gray-800 justify-center py-16 text-center">
            Loading..
        </div>
    </div>
</template>

<script>
import thread from '../services/thread'
import ThreadCard from '../components/thread/ThreadDetails.vue'
import CommentCard from '../components/post/CommentCard.vue'
import CommentItem from '../components/post/CommentItem.vue'

export default {
    data(){
        return {
            threadDetails: null,
            isLoading: true,
        }
    },
	components: {
		ThreadCard,
		CommentCard,
        CommentItem,
	},
    methods: {
        getThreadDetails(){
            const uuid = this.$route.params.idthread
            this.isLoading = false
            thread.getThread(uuid).then(({data}) => {
                const threads = data['thread'][0]
                const posts = data['post']

                console.log(threads)
                this.$store.commit('updateComments', posts)

				const date_options = { year: 'numeric', month: 'short' }
				const joined_date = new Date(threads['user__date_joined']).toLocaleDateString('en-us', date_options)

                this.threadDetails = threads
				this.threadDetails['user__date_joined'] = joined_date
            }).finally(() => this.isLoading = true)
        },
    },
    created(){
        this.getThreadDetails()
    }
}

</script>