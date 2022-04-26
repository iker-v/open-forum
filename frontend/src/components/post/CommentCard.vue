<template>
    <div class="flex flex-col gap-2 items-start justify-start bg-gray-50 rounded-lg px-3 py-2">
        <div class="flex items-center">
            {{ username }}
        </div>
        <textarea v-model="comment" placeholder="Comment here.." class="h-14 text-sm text-gray-800 w-full py-2 px-3 border rounded-lg"></textarea>
        <button @click="publishComment()" class="bg-blue-500 py-1.5 px-3 text-xs font-semibold rounded-lg text-white hover:bg-blue-600">
            Reply thread
        </button>
    </div>
</template>

<script>
    import post from '../../services/post'

    export default {
        data(){
            return {
                comment: ''
            }
        },
        props: ['username'],
        methods: {
            publishComment(){
                const formData = {
                    'uuid': this.$route.params.idthread,
                    'comment': this.comment
                }
                post.publishReply(formData).then(({data}) => {
                    this.$store.commit('updateComments', data)
                }).finally(() => this.comment = '')
            }
        }
    }

</script>