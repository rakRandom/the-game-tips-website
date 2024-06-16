<script>
    // Todo: Security test (text overflow, layout overflow, right position, responsivity etc)
    // Todo: Responsivity (follow mobile-first principles)
    // Todo: Add Black and White themes

    import { title } from './stores.js';
    import Header from './components/Header.svelte'
    import MainArticle from './components/landing_page/MainArticle.svelte';
    import SimpleSection from './components/SimpleSection.svelte';
    import BulletTipItem from './components/landing_page/BulletTipItem.svelte';
    import PopUpArticle from './components/PopUpArticle.svelte';

    import CategoryBar from './components/landing_page/CategoryBar.svelte';

    import Footer from './components/Footer.svelte';
</script>

<svelte:head>
    <title>{$title()}</title> 
</svelte:head>

<div class="w-full min-h-screen bg-[#001219]">
    <Header className="sticky top-0" />
    <MainArticle />

    <div class="mt-12">
        <SimpleSection 
            className="mt-8"
            title="Bullet Tips" 
            innerElements={[
                BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem, 
                BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem, BulletTipItem
            ]} 
        />

        <hr class="max-w-[1024px] mx-auto mt-14 mb-20">

        <SimpleSection 
            className="mt-4"
            title="Newest Posts" 
            innerElements={[
                PopUpArticle, PopUpArticle, PopUpArticle
            ]} 
        />
        <SimpleSection 
            className="mt-20"
            title="Newest Posts" 
            innerElements={[
                PopUpArticle, PopUpArticle, PopUpArticle
            ]} 
        />


    </div>

    <div class="mt-40">
        <div class="w-fit mx-auto">
            <h2 class="text-[#2EC4B6] text-[38px] font-normal">TIPS FOR YOUR GAME OF CHOICE</h2>
            <hr class="w-[75%] mx-auto border-[1px] border-[#2EC4B6]">
        </div>

        <div class="flex flex-col gap-[100px] mt-[100px]">
            <CategoryBar 
                
            />
            <CategoryBar 
                
            />
            <CategoryBar 
                
            />
        </div>
    </div>

    <Footer className="mt-40"/>
</div>


<style>
  
</style>
