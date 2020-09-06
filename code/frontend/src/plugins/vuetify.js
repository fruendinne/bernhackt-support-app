import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#242424',
                secondary: '#a5a5a5',
                accent: '#d40037',
                error: '#d40037',
                white: '#ffffff',
                black: '#000000',
            },
        },
    },
});
