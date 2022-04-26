<template>
    <div class="flex flex-col gap-5">
        <h1 class="text-gray-800 font-semibold text-2xl">Create a thread</h1>
        <div class="flex flex-col gap-5 bg-gray-100 shadow-sm rounded-xl py-3 px-5">
            <div class="flex flex-col gap-1">
                <label class="font-semibold">Title</label>
                <input v-model="thread.title" placeholder="Thread title.." class="py-2 px-4 rounded-xl border">
            </div>
            <div class="flex flex-col gap-1">
                <label class="font-semibold">Content</label>
                <textarea v-model="thread.content" placeholder="Thread content.." class="py-2 px-4 rounded-xl h-64 border"></textarea>
            </div>
            <button 
                @click.prevent="publishThread"
                class="flex items-center gap-1.5 py-2 px-4 self-start bg-blue-500 hover:bg-blue-600 rounded-lg text-white font-semibold"
            >
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
                Publish
            </button>     
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import thread from '../services/thread'

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

            thread.createThread(this.thread).then((response) => {
                this.$router.push({ name: 'ThreadView', params: { idthread: response.data['thread_id'] } })
            })
        }
    }
}

</script>  