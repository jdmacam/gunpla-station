const EventHandling = {
    data() {
      return {
        result: '0'
      }
    },
    methods: {
      roll() {
        this.result = Math.floor((Math.random() * 20)+1).toString(10)
        console.log('Rolled ' + this.result)
      }
    }
  }
  
  Vue.createApp(EventHandling).mount('#event-handling')