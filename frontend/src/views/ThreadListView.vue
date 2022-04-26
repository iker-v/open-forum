<template>
    <div class="flex flex-col">
        <div class="flex flex-col-reverse items-start gap-2 lg:flex-row lg:items-center lg:justify-between">
            <div class="flex bg-neutral-200 py-1.5 px-2 rounded-lg items-center gap-2">
                <button 
                    @click="menuTab = 0"
                    class="font-semibold py-1.5 px-3 rounded-lg text-sm"
                    :class="{'bg-blue-500 text-white': menuTab === 0, 'bg-white text-blue-500 border': menuTab !== 0}"
                >All</button>
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
        <div v-if="!isLoading" class="flex flex-col py-6 gap-2.5">
            <ThreadCard
                v-for="(thread, index) in threads"
                :key="index"
                :details="thread"
            />
            <div v-if="threads.length === 0" class="flex items-center justify-center py-6">
                <p class="text-2xl font-semibold text-gray-800">No threads have been found</p>
            </div>
        </div>
        <div class="mt-32" v-else>
            <SpinnerCard/>
        </div>
    </div>
</template>

<script>
    import ThreadCard from '../components/thread/ThreadCard.vue'
    import thread from '../services/thread'
    import SpinnerCard from '../components/SpinnerCard.vue'

    export default {
        components: {
            ThreadCard,
            SpinnerCard
        },
        data(){
            return{
                threads: [],
                menuTab: 0,
                category: '',
                numThreads: 10,
                isLoading: false,
            }
        },
        methods: {
            ThreadList(){
                this.isLoading = true
                this.category = this.$route.params.category
                thread.getThreadList(this.category, this.numThreads).then(({data}) => {
                    console.log(data)
                    this.threads.push(...data)
                }).finally(() => this.isLoading = false)
            },
            getMoreThreads(){
                window.onscroll = () => {
                    let scrollTop = document.documentElement.scrollTop
                    let innerHeight = window.innerHeight
                    let bottomOfWindow = scrollTop + innerHeight === document.documentElement.offsetHeight

                    if(bottomOfWindow){
                        ThreadList()
                    }
                }
            }
        },
        created() {
            this.ThreadList()
        },
        mounted() {
            this.getMoreThreads()
        },
}

</script>