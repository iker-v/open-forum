<template>
    <div class="relative">
        <button @click="showOptions = !showOptions" class="flex gap-2 bg-gray-100 py-1.5 px-3 text-sm lg:text-normal min-w-max w-24 rounded-lg items-center">
            <img v-if="$store.state.auth.image" src="$store.state.auth.image" class="h-6 w-6">
            {{ username }}
        </button>
        <div v-if="showOptions" v-click-away="onClickAway" class="absolute flex flex-col gap-2.5 w-full bg-gray-100 border py-3 px-2 rounded-b-lg">
            <router-link to="/settings" class="text-gray-800 flex items-center gap-1">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path></svg>
                Settings
            </router-link>
            <router-link to="/panel" class="text-gray-800 flex items-center gap-1">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z"></path></svg>
                Admin
            </router-link>
            <button @click="logout()" class="text-red-500 flex items-center gap-1">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z" clip-rule="evenodd"></path></svg>
                Logout
            </button>
        </div>
    </div>

</template>

<script>
    export default {
        data(){
            return {
                showOptions: false,
                username: '',
            }
        },
        methods: {
            onClickAway(event){
                this.showOptions = false
            },
            logout(){
                this.$store.commit('removeToken')
            },
            setUsername(){
                const user = localStorage.getItem("username")
                this.username = user
            }
        },
        created(){
            this.setUsername()
        }
    }
</script>