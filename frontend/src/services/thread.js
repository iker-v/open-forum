import axios from "axios";

const slash = '/thread'

export default {
    getThread(uuid){
        return axios.get(`${slash}/get-thread/${uuid}`)
    },
    searchThread(query){
        return axios.get(`${slash}/search-thread/${query}`)
    },
    createThread(formData){
        return axios.post(`${slash}/create-thread`, formData)
    },
    getThreadList(query, numThread){
        return axios.get(`${slash}/thread-list/${query}`)
    },
    upVote(query){
        return axios.post(`${slash}/up-vote/${query}`)
    },
    downVote(query){
        return axios.post(`${slash}/down-vote/${query}`)
    }
    
}