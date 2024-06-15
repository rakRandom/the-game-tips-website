<script>
    import { title } from './stores.js';
    import Header from './components/Header.svelte'
    import MainArticle from './components/landing_page/MainArticle.svelte';
</script>

<svelte:head>
    <title>{$title()}</title> 
</svelte:head>

<div class="w-full h-[3000px] bg-[#001219]">
    <Header className="sticky top-0"></Header>
    <MainArticle></MainArticle>
</div>


<style>
  
</style>
