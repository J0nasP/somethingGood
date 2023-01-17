<template>
    <form class="stack-small" @submit.prevent="onSubmit">
        <div>
           <label class="edit-label">Edit name for &quot; {{ label }} &quot;</label>
           <input
                :id="taskId"
                type="text"
                ref="labelInput"
                autocomplete="off"
                v-model.lazy.trim="newLabel"/> 
        </div>
        <div class="btn-group">
            <button type="button" class="btn" @click="onCancel">
                Cancel
                <span class="visually-hidden">editing {{ label }}</span>
            </button>
            <button type="submit" class="btn btn__primary">
                Save
                <span class="visually-hidden"> edit for {{ label }}</span>
            </button>
        </div>
    </form>
</template>

<script>
    export default {

        props:{
            label:{
                type: String,
                required: true,
            },
            taskId: {
                type: String,
                required: true,
            }
        },

        mounted(){
            const labelInputRef = this.$refs.labelInput;
            labelInputRef.focus();
        },

        data(){
            return {
                newLabel: this.label
            }
        },
        methods: {
            onSubmit(){
                if (this.newLabel && this.newLabel !== this.label) {
                    this.$emit("item-edited", this.newLabel);
                }
            },
            onCancel(){
                this.$emit("edit-cancelled")
            }
        },

    }
</script>

<style scoped>

.edit-label {
    font-family: Arial, sans-serif;
    color: black;
    display: block;
    margin-bottom: 5px;
}

input {
    display: inline-block;
    width: 100%;
    min-height: 0.4rem;
    padding: 0.4rem 0.8rem;
    border: 2px solid #565656;
}

form {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

form > * {
    flex: 0 0 100%;
}

</style>