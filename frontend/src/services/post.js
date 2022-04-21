import axios from "axios"

export default {
    publishReply(formData){
        return axios.post(`/post/publish-reply`, formData)
    },
    getComments(uuid){
        return axios.get(`/post/get-comments/${uuid}`)
    },
}