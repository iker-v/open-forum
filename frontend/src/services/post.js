import axios from "axios"

const slash = '/post'

export default {
    publishReply(formData){
        return axios.post(`${slash}/publish-reply`, formData)
    },
    getComments(uuid){
        return axios.get(`${slash}/get-comments/${uuid}`)
    },
}