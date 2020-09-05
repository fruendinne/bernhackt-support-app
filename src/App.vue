<template>
    <v-app>
        <v-app-bar color="white" app>
            <v-img
                    class="mx-2"
                    src="./assets/Quickline_Logo_RGB_positiv.png"
                    max-height="40"
                    max-width="80"
                    contain
            ></v-img>
            <v-spacer></v-spacer>
            <v-icon class="pa-2" color="black">
                mdi-magnify
            </v-icon>
            <v-icon color="black">
                mdi-menu
            </v-icon>
        </v-app-bar>
        <v-main>
            <v-container class="fill-height pa-0 align-start">
                <v-stepper v-model="e6" vertical class="elevation-0">
                    <v-stepper-step :complete="e6 > 1" step="1">Wo liegt das Problem?</v-stepper-step>
                    <v-stepper-content step="1">
                        <OnboardingProblemGeneral @select="e6 = 2"/>
                    </v-stepper-content>

                    <v-stepper-step :complete="e6 > 2" step="2">Verbindungsüberprüfung</v-stepper-step>
                    <v-stepper-content step="2">
                        <OnboardingCustomerNumber/>
                        <v-row no-gutters class="justify-end">
                            <v-btn text @click="e6 = 4">Überspringen</v-btn>
                            <v-btn medium color="accent" @click="e6 = 3">Weiter</v-btn>
                        </v-row>
                    </v-stepper-content>

                    <v-stepper-step :complete="e6 > 3" step="3">Überprüfung ist am Laufen</v-stepper-step>
                    <v-stepper-content step="3">
                        <OnboardingLoading v-if="e6 === 3" @ready="e6 = 4"/>
                    </v-stepper-content>

                    <v-stepper-step step="4">Überprüfung ist fertig</v-stepper-step>
                    <v-stepper-content step="4">
                      <RProjibliesmies/>
                      <v-row no-gutters class="justify-end">
                            <v-btn text @click="e6 = 3">Zurück</v-btn>
                            <v-btn color="accent" @click="e6 = 4">Weiter</v-btn>
                        </v-row>
                    </v-stepper-content>
                </v-stepper>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    import OnboardingCustomerNumber from './views/OnboardingCustomerNumber';
    import OnboardingProblemGeneral from './views/OnboardingProblemGeneral';
    import OnboardingLoading from './views/OnboardingLoading';
    import RProjibliesmies from '@/views/R-projibliesmies';

    export default {
        name: 'App',
        components: { OnboardingCustomerNumber, OnboardingProblemGeneral, OnboardingLoading, RProjibliesmies },
        data() {
            return {
                e6: 1,
            };
        },
    };
</script>

<style lang="scss">
    @import "sass/variables";

    .stepper--card {
        height: 350px !important;

        @media screen and(max-width: 800px) {
            height: 500px !important;
        }
    }
</style>
