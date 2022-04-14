<template>
      <router-link
        :to="{ name: 'threadList', params: { category: category.id }  }" 
        class="flex items-center gap-2 lg:gap-5 justify-center bg-gray-50 border-l-4 lg:border-l-8 border-blue-500 rounded-r-xl shadow-sm hover:bg-gray-100 py-1 lg:py-3 px-2 lg:px-6 w-full"
      >
        <div class="flex flex-col pr-1 lg:pr-3 w-3/4">
          <h2 class="lg:text-lg font-semibold text-gray-800">{{ category.name }}</h2>
          <p class="text-xs lg:text-sm truncate text-gray-600">{{ category.desc }}</p>
        </div>
        <div class="flex justify-end w-1/4">
          <img v-if="category.image" class="h-16 rounded object-cover" :src="category.image">
        </div>
      </router-link>
</template>

<script>
    export default {
        props: ['category']
    }
</script>
