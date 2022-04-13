import axios from "axios";

export default {
    getThread(uuid){
        console.log(uuid)
        return axios.get(`/get-thread/${uuid}`)
    },
    searchThread(query){
        return axios.get(`/search-thread/${query}`)
    },
    publishReply(uuid, reply){

        const formData = {
            'thread_uuid': uuid,
            'comment': reply
        }

        return axios.post(`/publish-reply`, formData)
    },
    getComments(uuid){
        return axios.get(`/get-comments/${uuid}`)
    }
}