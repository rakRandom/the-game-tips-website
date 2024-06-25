<script>
    import Footer from "../components/Footer.svelte";
    import Header from "../components/Header.svelte";
    import Section from "../components/help/Section.svelte";

    let values = [
        {
            legend: "Account", 
            contents: [
                [
                    "How to create an account", 
                    "Lorem Ipsum"
                ], 
                [
                    "Password lost", 
                    "Lorem Ipsum"
                ], 
                [
                    "Account Hacked", 
                    "Lorem Ipsum"
                ], 
                [
                    "Delete account", 
                    "Lorem Ipsum"
                ]
            ]
        }, 
        {
            legend: "Content Creation", 
            contents: [
                [
                    "How to be a creator", 
                    "Lorem Ipsum"
                ], 
                [
                    "How to make an article", 
                    "Lorem Ipsum"
                ], 
                [
                    "How payment works", 
                    "Lorem Ipsum"
                ], 
                [
                    "Be a verified creator", 
                    "Lorem Ipsum"
                ]
            ]
        }, 
    ];
</script>

<div class="flex flex-col w-full min-h-screen bg-[#F6F6F6] dark:bg-[#000B10] text-color-body">
    <Header className="sticky top-0" />
    <main class="flex flex-col gap-32 flex-1 max-w-[1024px] w-full mx-auto py-24">
        <div class="dark:bg-[#001A24] bg-[#EEE] py-16 w-full px-8">
            <h1 class="text-4xl text-color-title font-title-semibold mb-16">
                Help Center
            </h1>
    
            <p class="text-[1.2rem] px-4">
                If you need assistance with our services or tools, you’ve come to the right place. We strive to make your experience even better, so we make it easy for you to get help and support.
            </p>
    
            <p class="text-[1.2rem] px-4 mt-4">
                Here you can get help in any way you like by reading how our tools work or talking to our support team.
            </p>
        </div>
        
        {#each values as value}
        <Section {...value} />
        {/each}
    </main>
    <Footer />
</div>

<style>

</style>
