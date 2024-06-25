<script>
  import { apiLink } from "../stores";

    let confirmed = false;

    function confirmCredentials() {}

    async function getContent() {
        let path = document.getElementById("url").value;
        let payload = await fetch($apiLink + "json" + path);
        let content = await payload.json();

        if (!content)
            return;

        document.getElementById("content").innerHTML = JSON.stringify(content, null, 4);
    }

    async function putContent() {
        let path = document.getElementById("url").value;
        let content = document.getElementById("content").value;

        return await fetch($apiLink + "json" + path, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-type':'application/json', 
                'Accept':'application/json'
            },
            body: JSON.stringify({
                content: content
            })
        });
    }
</script>

<div class="w-full h-svh bg-color-0">
    {#if !confirmed}
    <div class="flex items-center justify-center w-full h-full">
        <div class="flex flex-col gap-8 w-fit h-fit p-10 mb-20 border border-[#1E9B8F] dark:border-[#69D3C9] rounded-lg">
            <h1 class="font-title-medium text-color-title text-4xl text-center">
                Login
            </h1>
    
            <div class="flex flex-col gap-4 text-[#000B10] text-lg *:*:outline-none">
                <div>
                    <label for="email" class="block text-color-title">Email</label>
                    <input type="email" name="email" id="" class="w-[250px] px-2 py-1 border-b-2 border-[#1E9B8F] dark:border-[#69D3C9] rounded-md">
                </div>
                
                <div>
                    <label for="password" class="block text-color-title">Password</label>
                    <input type="password" name="password" id="" class="w-[250px] px-2 py-1 border-b-2 border-[#1E9B8F] dark:border-[#69D3C9] rounded-md">
                </div>
            </div>
    
            <button type="button" id="confirm-button" on:click={() => {confirmed = !confirmed}}
                class="text-lg w-full p-2 border border-[#1E9B8F] dark:border-[#69D3C9] hover:bg-[#69D3C9] hover:text-black">
                Confirm
            </button>
        </div>
    </div>
    {:else}
    <div class="mx-auto w-full max-w-[1280px] h-fit p-10">
        <h1 class="font-title-medium text-color-title text-4xl text-center">
            Admin
        </h1>

        <div class="flex flex-col gap-4 mt-6 text-lg" >
            <div>
                <label for="url" class="block text-color-title">URL</label>
                <div class="flex gap-4 w-full">
                    <input type="url" name="url" id="url" value="/" class="flex-1 text-black w-[800px] h-full px-2 py-3 rounded-md outline-none">
                    <div class="inline *:py-2 *:px-4 *:border *:border-[#1E9B8F] dark:*:border-[#69D3C9] *:rounded-lg hover:*:bg-[#69D3C9] hover:*:text-black">
                        <button type="button" on:click={getContent}>GET</button>
                        <button type="submit" on:click={putContent}>PUT</button>
                    </div>
                </div>
            </div>

            <div>
                <label for="json" class="block text-color-title">Content</label>
                <textarea name="json" id="content" class="text-base text-black w-full max-w-[1280px] min-h-[500px] p-2 rounded-md outline-none overflow-y-auto"></textarea>
            </div>
        </div>
    </div>
    {/if}
</div>

<style>
  
</style>
