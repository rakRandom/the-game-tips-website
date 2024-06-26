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
                    "Click on the user icon in the top right corner of the screen and then on \"sign up\" or scroll down to the footer and click on the \"login\" link, fill in the information requested on the registration form and click on \"create account\""
                ], 
                [
                    "Password lost", 
                    "Click on the user icon in the top right corner of the screen and then on \"settings\", there you will find the option to modify your password, where you will only need to confirm the operation via email to reset the password. If the password is lost during sign in, there is a small caption that contains the text \"forgot password?\", clicking on it takes you to the same need to confirm the operation by email and then modify your password."
                ], 
                [
                    "Account Hacked", 
                    "In \"our team\" you can chat directly with us and our technical support and request deactivation and verification of your account, which will be done as soon as possible"
                ], 
                [
                    "Delete account", 
                    "Click on the user icon and then select \"my account\", scrolling down the screen you can find a button responsible for deleting your account."
                ]
            ]
        }, 
        {
            legend: "Content Creation", 
            contents: [
                [
                    "How to be a creator", 
                    "In \“our team\” you can chat directly with us and inform us that you want to be a content creator for our platform, we will investigate the request and get back to you as soon as possible"
                ], 
                [
                    "How to make an article", 
                    "When becoming an article creator, a new selection opens when clicking on the user icon and a new link appears in the footer at the bottom of the page, where these selections lead to a development region within our site that allows writing and editing, uploading articles produced on another platform and finally posting the materials."
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
