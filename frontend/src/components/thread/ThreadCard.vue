<template>
        <div class="flex flex-col w-full bg-gray-50 border rounded-lg">
            <div class="flex">
                <div class="bg-gray-100 rounded-l-lg w-0.5/12">
                    <ThreadRate
						:uuid="thread.uuid"
						:upvote="thread.upvote"
						:downvote="thread.downvote"  
                        :checkup="thread.checkup"
                        :checkdown="thread.checkdown"                      
                    />
                </div>
                <div class="flex px-2 w-9/12">
                
                    <router-link 
                        :to="{ name: 'ThreadView', params: { id: thread.uuid } }"
                        class="flex flex-col gap-1 py-2 items-start justify-start"
                    >
                        <div class="inline-flex">
                            <h2 class="font-bold inline-flex text-xl break-all text-gray-800">{{ thread.title }}</h2>
                        </div>
                        
                        <p class="text-gray-700 truncate text-sm"> {{ thread.desc }} </p>
                    </router-link>
                </div>
                <div class="flex w-2.5/12">
                    <img class="rounded object-cover" src="">
                </div>
            </div>

            <div class="flex py-1 px-3 rounded-b-lg items-center gap-3 bg-gray-100">
                <router-link
                    :to="{ name: 'ThreadView', params: { id: thread.uuid } }"
                    class="flex gap-1 items-center font-semibold text-sm text-gray-700">
                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z" clip-rule="evenodd"></path></svg>
                        <span>({{ thread.post }})</span>
                        <p>Comments</p>
                </router-link>
            </div>
        </div>
</template>

<script>
    import ThreadRate from './ThreadRate.vue'
   
    export default {
        props: ['thread'],
        components: {
            ThreadRate
        }
    }

</script>