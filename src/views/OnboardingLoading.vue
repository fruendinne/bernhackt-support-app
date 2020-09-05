<template>
    <v-app>
        <div>
            <h3>Wir überprüfen nun Ihre Verbindung zu unseren Systemen. Bitte haben Sie einen Moment Geduld.</h3>
            <v-row align-content="center" justify="center">
                <v-col cols="6">
                    <v-progress-linear
                            indeterminate
                            color="red"
                            rounded
                            height="6"
                            class="progress--bar"
                    ></v-progress-linear>
                </v-col>
            </v-row>
        </div>
    </v-app>
</template>

<script>
    export default {
        props: {},
    };
</script>

<style>
    .progress--bar {
        margin-top: 96px;
    }
</style>
