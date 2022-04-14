<template>
    <div v-if="this.$store.state.auth.showRegister" className="flex justify-center bg-black bg-opacity-70 items-center overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div v-click-away="onClickAway" className="relative opacity-100 w-auto my-6 mx-auto max-w-2xl">
            <div className="border-0 p-5 rounded-lg shadow relative flex flex-col gap-3 w-full bg-white outline-none focus:outline-none">

                    <div class="flex items-center justify-center" v-if="errors.length">
                        <p
                            v-for="error in errors"
                            :key="error"
                        >
                            {{error}}
                        </p>
                    </div>
                    <form class="flex flex-col gap-5 shadow-sm rounded-xl px-12 py-2" @submit.prevent="submitForm" >
                        <h2 class="font-bold text-2xl text-gray-800 text-center">Register</h2>
                        <div class="flex gap-0.5 flex-col">
                            <label class="text-sm font-semibold text-gray-800">Username</label>
                            <input type="text" class="py-2 px-3 bg-gray-50 border text-sm rounded-lg" v-model="username">
                        </div>
                        <div class="flex gap-0.5 flex-col">
                            <label class="text-sm font-semibold text-gray-800">Email</label>
                            <input type="email" class="py-2 px-3 bg-gray-50 border text-sm rounded-lg" v-model="email">
                        </div>
                        <div class="flex gap-0.5 flex-col">
                            <label class="text-sm font-semibold text-gray-800">Password</label>
                            <input type="password" class="py-2 px-3 bg-gray-50 border text-sm rounded-lg" v-model="password">
                        </div>
                        <div class="flex">
                            <button class="bg-blue-500 shadow w-full text-sm py-2 hover:bg-blue-600 text-white font-semibold rounded-lg" type="submit">Register</button>
                        </div>
                    </form>                           
            </div>
        </div>
    </div>
</template>

<script>
    import auth from '../../services/auth'

    export default {
        name: 'SignUpView',
        data(){
            return {
                username: '',
                email: '',
                password: '',
                errors: []
            }
        },
        methods: {
            onClickAway(event){
                this.$store.commit('changeShowRegister')
            },
            submitForm(e) {
                auth.register(this.username, this.email, this.password).then(response => {
                    console.log(response)
                    this.$store.commit('changeShowRegister')
                    this.$store.commit('initializeStore')
                }).catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data))
                    } else if (error.message) {
                         console.log(JSON.stringify(error.message))
                    } else {
                        console.log(JSON.stringify(error))
                    }
                })
                    
            }
        }
}
</script>