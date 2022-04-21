import axios from "axios";

export default {
    getThread(uuid){
        return axios.get(`/thread/get-thread/${uuid}`)
    },
    searchThread(query){
        return axios.get(`/thread/search-thread/${query}`)
    },
    createThread(formData){
        return axios.post('/thread/create-thread', formData)
    },
    getThreadList(query){
        return axios.get(`/thread/thread-list/${query}`)
    },
    upVote(query){
        return axios.post(`/thread/up-vote/${query}`)
    },
    downVote(query){
        return axios.post(`/thread/down-vote/${query}`)
    }
    
}