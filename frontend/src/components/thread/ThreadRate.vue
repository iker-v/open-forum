<template>
    <div class="flex flex-col p-3 items-center justify-between">
        <button
            :class="{'w-6 h-6 text-blue-500': check_up, 'h-6 w-6': !check_up }"
            @click="up()"
        >
                <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
        </button>
        <p class="text-sm font-semibold text-blue-500">{{ total() }}</p>
        <button @click="down()">
            <svg :class="{'w-6 h-6 text-blue-500': check_down, 'h-6 w-6': !check_down }" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
        </button>
    </div> 
</template>

<script>
    import thread from '../../services/thread'


    export default {
        data(){
            return {
                upvotes: this.upvote,
                downvotes: this.downvote,
                check_up: this.checkup,
                check_down: this.checkDown,
            }
        },
        props: ['uuid', 'upvote', 'downvote', 'checkup', 'checkdown'],
        methods: {
            up(){
                thread.upVote(this.uuid).then(({data}) => {
                    console.log(data)
                    this.check_up = !this.check_up
                    this.check_down = false
                    this.upvotes = data['up_votes']
                    this.downvotes = data['down_votes']
                })
            },
            down(){
                thread.downVote(this.uuid).then(({data}) => {
                    this.check_up = false
                    this.check_down = !this.check_down 
                    this.upvotes = data['up_votes']
                    this.downvotes = data['down_votes']
                })
            },
            total(){
                return this.upvotes - this.downvotes
            }
        },
    }

</script>