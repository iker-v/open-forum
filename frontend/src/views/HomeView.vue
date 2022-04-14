<template>
  <div class="flex flex-wrap gap-3 items-center">
    <div v-if="isLoading" class="flex items-center">
      <p>Loading..</p>
    </div>

      <CategoryCard
        v-for="(category, index) in categories" 
        :category="category"
        :key="index"
      />
  </div>

</template>
<script>
  import CategoryCard from '../components/category/CategoryCard.vue'
  import category from '../services/category'

  export default {
    components: {
      CategoryCard
    },
    data(){
      return {
        categories: [],
        isLoading: false,
      }
    },
    methods: {
      getCategoryList(){
        category.getCategories().then(({data}) => {
          this.categories = data
        })
      }
    },
    created() {
      this.getCategoryList()
    }
  }

</script>
