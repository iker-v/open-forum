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
  import axios from 'axios'
  import CategoryCard from '../components/category/CategoryCard.vue'

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
      getCategories(){
        axios.get('/get-categories')
        .then(({data}) => {
          this.categories = data
        })
        .finally(() => this.isLoading)
      }
    },
    created() {
      this.getCategories()
    }
  }

</script>
