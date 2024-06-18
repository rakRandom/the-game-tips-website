<script>
  import Header from "../components/Header.svelte";
  import HeadlineTemplate from "../components/article_page/HeadlineTemplate.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<div
  class="w-full min-h-screen bg-[#F6F6F6] dark:bg-[#000B10] text-[#121212] dark:text-white"
>
  <Header className="sticky top-0" />
  <HeadlineTemplate />
  <main class="flex flex-col gap-16 flex-1 max-w-[1024px] w-full mx-auto py-24">
    <div class="justify-center">
      <p class="text-2xl text-justify">
        If you want a melee build in Elden Ring, it's a good idea to invest
        points in strength or dexterity. This helps meet the minimum
        requirements for many weapons and also increases the damage done by
        them.
      </p>
    </div>
    <div>
        <p></p>
    </div>
  </main>
  <Footer />
</div>
