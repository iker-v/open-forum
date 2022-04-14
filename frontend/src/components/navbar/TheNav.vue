<template>
    <nav className="mx-auto flex justify-between w-full max-w-3xl">
      <router-link to="/" class="flex gap-2 items-center">
        <svg class="w-6 h-6 text-neutral-800" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"></path></svg>
        <h1 className="uppercase font-bold leading-none text-xl text-neutral-800">Open forum</h1>
      </router-link>

      <SearchThread/>

      <div v-if="!this.$store.state.auth.isAuthenticated" className="flex items-center">
        <div className="flex gap-2 items-center">
            <button @click="changeShowRegister()" className="py-1.5 px-4 bg-blue-500 rounded-lg text-white font-semibold">Sign up</button>
            <button @click="changeShowLogin()" className="py-1.5 px-4 bg-white rounded-lg text-neutral-800 font-semibold shadow-sm">Log in</button>
        </div>
        <RegisterModal/>
        <LoginModal/>
      </div>
      <div v-else>
        <UserDropdown/>
      </div>
    </nav>
</template>

<script>
  import SearchThread from './SearchThread.vue'
  import RegisterModal from '../auth/RegisterModal.vue'
  import LoginModal from '../auth/LoginModal.vue'
  import UserDropdown from './UserDropdown.vue'
  import { mapMutations } from 'vuex'

  export default {
    components: {
      SearchThread,
      RegisterModal,
      LoginModal,
      UserDropdown,
    },
    methods: {
      ...mapMutations([
        'changeShowRegister',
        'changeShowLogin'
      ])
    }
  }


</script>