<template>
    <div class="flex flex-col gap-5 bg-gray-50 shadow-sm rounded-xl py-3 px-5">
        <div class="flex flex-col gap-1">
            <label class="font-semibold">Title</label>
            <input v-model="thread.title" placeholder="Thread title.." class="py-2 px-4 rounded-xl border">
        </div>
        <div class="flex flex-col gap-1">
            <label class="font-semibold">Content</label>
            <textarea v-model="thread.content" placeholder="Thread content.." class="py-2 px-4 rounded-xl h-64 border"></textarea>
        </div>
         <button @click.prevent="publishThread" class="py-2 px-6 self-start bg-blue-500 hover:bg-blue-600 rounded-lg text-white font-semibold">Publish</button>     
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return{
            thread: {
                title: '',
                content: '',
                category: '',
            },

        }
    },
    methods: {
        publishThread(){

            this.thread.category = this.$route.params.categoryid

            axios.post('/create-thread', this.thread)
            .then((response) => {
                this.$router.push({ name: 'ThreadView', params: { id: response.data['thread_id'] } })
            })
        }
    }
}

</script>  