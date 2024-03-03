<template>
  <div class="rounded-container boards">
    <h3>Boards</h3>
    <button  @click="$emit('switchboard','general')" selected="selected" :class="{selected:board==='general'}">General</button>
    <button @click="$emit('switchboard','animals')" :class="{selected:board==='animals'}">Animals</button>
    <button @click="$emit('switchboard','art')" :class="{selected:board==='art'}">Art</button>
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
    .selected{
	text-decoration: underline;
    }
</style>
