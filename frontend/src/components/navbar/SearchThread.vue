<template>
      <div className="flex flex-col items-center" v-click-away="onClickAway">
        <div class="flex items-center">
          <input @keyup="searchQuery" v-model="query" placeholder="Search a thread.." className="py-1.5 px-3 border-l border-b border-t focus:outline-none rounded-l-lg"/>
          <button className="py-1.5 px-3 bg-white border-r border-b border-t rounded-r-xl">
            <svg class="w-6 h-6 text-neutral-800" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path></svg>
          </button>
        </div>
        <div class="relative w-full">
          <div v-if="isSearching" class="absolute bg-gray-50 border-b border-r border-l py-3 w-full rounded-b-xl">
            <div v-show="data.length > 0" class="flex flex-col py-4">
              <router-link
                v-for="thread in data"
                :key="thread.uuid"
                :to="{ name: 'ThreadView', params: { id: thread.uuid }  }"
              >
                <div @click="onClickAway" class="flex hover:bg-gray-100 py-2 px-1.5 items-center justify-between">
                  <p class="text-sm font-semibold text-gray-800">{{ thread.title }}</p>
                  <p class="text-xs text-gray-600">{{ new Date(thread.created_at).toLocaleString('es-en', {'dateStyle' : 'short'}) }}</p>
                </div>
              </router-link>
            </div>
            <div class="flex justify-center py-4" v-show="data.length === 0">
              <p class="text-sm font-semibold text-gray-700">No results found</p>
            </div>
          </div>
        </div>


      </div>
</template>

<script>
  import thread from '../../services/thread'

  export default {
    data(){
      return {
        isLoading: false,
        data: [],
        isSearching: false,
      }
    },
    methods: {
      onClickAway(event) {
          this.isSearching = false
          this.query = ''
      },
      searchQuery(){
        if (this.query.length > 3){
          this.isSearching = true
          this.isLoading = true
          thread.searchThread(this.query).then(({data}) => {
            this.data = data
            console.log(data)
          }).finally(() => this.isLoading = false)
        }

      }
    },
  }


</script>  