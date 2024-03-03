<template>
<div class="rounded-container boards">
  <h3>Boards</h3>
  <button  @click="$emit('switchboard','general')" selected="selected" :class="{selected:board==='general'}">General</button>
  <button @click="$emit('switchboard','animals')" :class="{selected:board==='animals'}">Animals</button>
  <button @click="$emit('switchboard','art')" :class="{selected:board==='art'}">Art</button>
<select @change="$emit('switchboard', $event.target.value)">
  <option value="general" :selected="board==='general'">General</option>
  <option value="animals" :selected="board==='animals'">Animals</option>
  <option value="art" :selected="board==='art'">Art</option>
</select>
</div>
  

  
</template>

<script>
export default {
    name : 'Board',
    props: {
	board: String,
    }
}
</script>
<style scoped>
    .boards{
	display : flex;
	flex-direction : column;
	margin-bottom:15px;
    }
    button{
	border : none;
	border-radius: 0;
	font-size:1.2rem;
	}
 

    /* CSS for Desktop View */
@media (min-width: 769px) {
    .boards {
        display: flex;
        flex-direction: column;
    }

    .boards button {
        margin-bottom: 5px; /* Adjust the spacing between buttons if needed */
    }
    .boards select {
        display: none;
    }
       .selected{
	text-decoration: underline;
    }
}

/* CSS for Mobile View */
@media (max-width: 768px) {
    .boards {
        display: block;
    }
    h3 {
    display:none;}

    .boards button {
        display: none;
    }

    /* Style for the select input */
    .boards select {
        width: 100%;
        padding: 8px;
        margin-bottom: 10px; /* Adjust the spacing if needed */
    }
}
</style>
