<template>
    <div class="flex flex-col">
        <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
                <button 
                    @click="menuTab = 1"
                    class="font-semibold py-1.5 px-3 rounded-lg text-sm"
                    :class="{'bg-blue-500 text-white': menuTab === 1, 'bg-white text-blue-500 border': menuTab !== 1}"
                >Most commented</button>
                <button
                    @click="menuTab = 2"
                    class="font-semibold py-1.5 px-3 rounded-lg text-sm"
                    :class="{'bg-blue-500 text-white': menuTab === 2, 'bg-white text-blue-500 border': menuTab !== 2}"
                >Most upvoted</button>
            </div>
            <div>
                <router-link 
                    :to="{ name: 'createThread', params: { categoryid: category }}"
                    v-if="this.$store.state.auth.isAuthenticated"
                    class="py-1.5 px-3 flex items-center gap-1 bg-blue-500 hover:bg-blue-600 rounded-lg text-white font-semibold">
                    <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"></path></svg>
                    Create thread
                </router-link>
            </div>
        </div>
        <div class="flex py-5 flex-col">
            <div v-if="threadList.length === 0" class="flex items-center justify-center py-6">
                <p class="text-2xl font-semibold text-gray-800">No threads have been found</p>
            </div>
        </div>
        <div class="flex flex-col gap-2.5">
            <ThreadCard
                v-for="(thread, index) in threadList"
                :key="index"
                :thread="thread"
            />
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import { useRoute } from 'vue-router'
import ThreadCard from '../components/thread/ThreadCard.vue'

export default {
    components: {
        ThreadCard
    },
    data(){
        return{
            threadList: [],
            menuTab: 0,
            category: '',
        }
    },
    methods: {
        getThreadList(){
            const route = useRoute()
            this.category = route.params.category
            axios.get(`/thread-list/${this.category}`)
            .then(({data}) => {
                this.threadList = data
            })
        }
    },
    created() {
        this.getThreadList()
    },
}

</script>