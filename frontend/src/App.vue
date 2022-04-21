<template>
  <main>
    <header class="flex bg-neutral-800 w-full py-4 mx-auto">
      <TheNav/>
    </header>
    <section class="flex flex-col max-w-3xl py-6 px-2 mx-auto">
      <RouterView />
    </section>
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