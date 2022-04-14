export default {
    publishReply(uuid, reply){
        const formData = {
            'thread_uuid': uuid,
            'comment': reply
        }

        return axios.post(`/publish-reply`, formData)
    },
    getComments(uuid){
        return axios.get(`/get-comments/${uuid}`)
    },
}