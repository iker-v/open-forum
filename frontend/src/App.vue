<template>
  <header class="flex bg-white border-b-2 w-full py-4 mx-auto">
    <TheNav/>
  </header>
  <main class="flex flex-col max-w-3xl py-6 px-2 mx-auto">
    <RouterView />
  </main>
</template>

<script>
import TheNav from './components/navbar/TheNav.vue'

export default {
  components: {
    TheNav,
  }
}

</script>