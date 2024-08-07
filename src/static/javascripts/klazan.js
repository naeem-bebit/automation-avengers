const { createApp, ref } = Vue 

const App = {
  data() {
    return { 
      prayerTime: [] 
    }
  },
  delimiters: ["[[", "]]"],
  created() {
    this.getData();
  },
  methods: {
    getData() {
          fetch('https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=week&zone=WLY01')
              .then((response) => response.json())
              .then((data) => 
              {
                this.prayerTime = data.prayerTime;
                console.log(this.prayerTime)
              });
      }   
  }  
}

const app = createApp(App)
app.mount('#app')