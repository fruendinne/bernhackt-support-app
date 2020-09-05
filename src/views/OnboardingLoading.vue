<template>
    <div>
        <h3>Wir überprüfen nun Ihre Verbindung zu unseren Systemen. Bitte haben Sie einen Moment Geduld.</h3>
        <v-row align-content="center" justify="center" class="mb-4">
            <v-col class="pr-5 pr-sm-0">
                <v-progress-linear
                  indeterminate
                  color="accent"
                  rounded
                  height="6"
                  class="progress--bar"
                ></v-progress-linear>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    export default {
        props: {},
        mounted () {
            setTimeout(
              () => { this.$emit('ready') },
              5000
            )
        }
    };
</script>

<style>
    .progress--bar {
        margin-top: 1rem;
    }
</style>
