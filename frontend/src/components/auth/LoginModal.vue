<template>
    <div v-if="this.$store.state.auth.showLogin" className="flex justify-center bg-black bg-opacity-70 items-center overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div v-click-away="onClickAway" className="relative opacity-100 w-auto my-6 mx-auto max-w-2xl">
            <div className="border-0 p-5 rounded-lg shadow relative flex flex-col gap-3 w-full bg-white outline-none focus:outline-none">
                <form class="flex flex-col gap-5" @submit.prevent="submitForm" >
                    <div class="flex items-center justify-center" v-if="errors.length">
                        <p
                            v-for="error in errors"
                            :key="error"
                        >
                            {{error}}
                        </p>
                    </div>
                    <h2 class="flex items-center justify-center text-center font-bold text-2xl text-gray-800">
                        <svg class="w-12 h-12" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path></svg>
                        Login
                    </h2>
                    <div class="flex flex-col gap-1">
                        <label class="text-sm font-semibold text-gray-800">Email</label>
                        <input 
                            type="email"
                            placeholder="user@gmail.com"
                            class="py-1.5 px-3 bg-gray-50 border rounded-lg"
                            v-model="email"
                        >
                    </div>
                    <div class="flex flex-col gap-1">
                        <label class="text-sm font-semibold text-gray-800">Password</label>
                        <input
                            type="password"
                            placeholder="**********"
                            class="py-1.5 px-3 bg-gray-50 border rounded-lg"
                            v-model="password"
                        >
                    </div>
                    <button class="py-1.5 px-3 rounded-lg bg-blue-500 hover:bg-blue-600 font-semibold text-white" type="submit">Login</button>
                </form>                            
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import auth from '../../services/auth'

    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                email: '',
                password: '',
                errors: [],
            }
        },
        methods: {
            onClickAway(event) {
                this.$store.commit('changeShowLogin')
            },
            submitForm(e){
                axios.defaults.headers.common["Authorization"] = ""
                localStorage.removeItem("token")

                auth.login(this.email, this.password)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common["Authorization"] = "Token " + token
                        this.$store.commit('initializeStore')

                        axios.get('/account/users/me').then(({data}) => {
                            this.$store.commit('setUser', data['username'])
                            localStorage.setItem("username", data['username'])
                        }).finally(() => this.$store.commit('changeShowLogin'))
                    })
                    .catch(error => {
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