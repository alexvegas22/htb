<template>
  <div class="rounded-container boards">
    <h3>Boards</h3>
    <a @click="$emit('switchboard','general')" selected="selected">General</a>
    <a @click="$emit('switchboard','animals')" >Animals</a>
    <a @click="$emit('switchboard','art')">Art</a>
  </div>
</template>

<script>
export default {
    name : 'Board',

}
</script>
<style scoped>
    .boards{
	display : flex;
	flex-direction : column;
	margin-bottom:15px;
    }
    a{
    color:var(--text)}
    .selected{
	text-decoration: underline;
    }
</style>
