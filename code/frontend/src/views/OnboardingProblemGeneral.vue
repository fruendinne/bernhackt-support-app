<template>
    <div class="d-flex flex-column">
        <v-row no-gutters>
            <h3>Zu welchem Thema benötigen Sie Hilfe?</h3>
        </v-row>
        <div>
            <v-row>
                <v-col class="pa-0" cols="6" md="3"
                       @click="$emit('select', 'internet')"
                >
                    <div class="sexschen-button">
                        <v-avatar class="ma-2" size="5rem" color="gray">
                          <img
                              src="../assets/wifiicon.png">
                        </v-avatar>
                        <span>Internet</span>
                    </div>
                </v-col>
                <v-col class="pa-0" cols="6" md="3"
                       @click="$emit('select', 'tv')"
                >
                    <div class="sexschen-button">
                      <v-avatar class="ma-2" size="5rem" color="gray">
                        <img
                            src="../assets/tvicon.png">
                      </v-avatar>
                        <span>TV</span>
                    </div>
                </v-col>
                <v-col class="pa-0" cols="6" md="3"
                       @click="$emit('select', 'mobile')"
                >
                    <div class="sexschen-button">
                      <v-avatar class="ma-2" size="5rem" color="gray">
                        <img
                            src="../assets/mobileicon.png">
                      </v-avatar>
                        <span>Mobile</span>
                    </div>
                </v-col>
                <v-col class="pa-0" cols="6" md="3"
                       @click="$emit('select', 'festnetz')"
                >
                    <div class="sexschen-button">
                      <v-avatar class="ma-2" size="5rem" color="gray">
                        <img
                            src="../assets/festnetzicon.png">
                      </v-avatar>
                        <span>Festnetz</span>
                    </div>
                </v-col>
            </v-row>
        </div>
    </div>
</template>

<script>
    export default {
        props: {},
    };
</script>

<style lang="scss">
    .sexschen-button {
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #d40037;
        font-size: 1.25rem;
    }
</style>
