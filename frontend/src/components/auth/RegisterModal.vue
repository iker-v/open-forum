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
                        <h2 class="flex items-center justify-center text-center font-bold text-2xl text-gray-800">
                            <svg class="w-12 h-12" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path></svg>
                            Register
                        </h2>
                        <div class="flex gap-0.5 flex-col">
                            <label class="text-sm font-semibold text-gray-800">Username</label>
                            <input
                                type="text"
                                placeholder="username"
                                class="py-2 px-3 bg-gray-50 border text-sm rounded-lg"
                                v-model="username"
                            >
                        </div>
                        <div class="flex gap-0.5 flex-col">
                            <label class="text-sm font-semibold text-gray-800">Email</label>
                            <input
                                type="email"
                                placeholder="user@gmail.com"
                                class="py-2 px-3 bg-gray-50 border text-sm rounded-lg"
                                v-model="email"
                            >
                        </div>
                        <div class="flex gap-0.5 flex-col">
                            <label class="text-sm font-semibold text-gray-800">Password</label>
                            <input 
                                type="password"
                                placeholder="*********"
                                class="py-2 px-3 bg-gray-50 border text-sm rounded-lg"
                                v-model="password"
                            >
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