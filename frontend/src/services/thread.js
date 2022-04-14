import axios from "axios";

export default {
    getThread(uuid){
        console.log(uuid)
        return axios.get(`/get-thread/${uuid}`)
    },
    searchThread(query){
        console.log(query)
        return axios.get(`/search-thread/${query}`)
    },

    
}