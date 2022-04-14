<template>
    <div class="flex flex-col">
		<div v-if="isLoading" class="flex flex-col gap-5">
			<ThreadCard :threadDetails="threadDetails" />
			<div v-if="$store.state.auth.isAuthenticated">
				<PostComment :username="threadDetails.username" />
			</div>
            <div 
                v-for="(co, index) in comments"
                :key="index"
                class="flex flex-col border-l-2 pl-2 py-1">
                <div class="flex items-end gap-2">
                    <h3 class="text-blue-500 font-semibold"> @{{ co.user__username }} </h3>
                    <p class="text-xs font-semibold py-0.5 text-gray-400"> {{ new Date(co.date).toLocaleDateString('en-us', { year: 'numeric', month: 'short', day: 'numeric' }) }} </p>
                </div>
                <div class="py-1">
                    <p class="text-gray-900"> {{ co.comment }} </p>
                </div>
            </div>
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
import PostComment from '../components/post/PostComment.vue'

export default {
    data(){
        return {
            threadDetails: null,
            isLoading: true,
            comments: [],
        }
    },
	components: {
		ThreadCard,
		PostComment,
	},
    methods: {
        getThreadDetails(){
            const uuid = this.$route.params.id
            this.isLoading = false
            thread.getThread(uuid).then(({data}) => {
                const threads = data['thread'][0]
                const posts = data['post']

                this.comments = posts

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