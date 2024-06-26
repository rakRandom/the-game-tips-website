<script>
    import Footer from "../components/Footer.svelte";
    import Header from "../components/Header.svelte";
    import FavoriteGames from "../components/user_page/FavoriteGames.svelte";
  import { apiLink } from "../stores";

    export let params = {};
    let isUser = params.id.split("i")[0];
    let userID = params.id.split("i")[1];

    var editingname = false, editingbio = false, biolength;

    let content = {
        name: "",
        bio: ""
    };

    getContent();

    async function getContent() {
        let payload = await fetch($apiLink + "user/" + userID);
        let request = await payload.json();

        if (!request)
            return;

        content = request;
    }

    function editName() {
        var usernamediv = document.getElementById('usernamediv');
        var usernametext = document.getElementById('usernametext');
        var usernameinput = document.getElementById('usernameinput');
        var usernameediticon = document.getElementById('usernameediticon');

        editingname = !editingname;

        if (editingname == true) {
            usernamediv.classList.add('bg-color-mid', 'border-b-2', 'border-l-2', 'border-[#69D3C9]')
            usernameinput.classList.remove('hidden');
            usernametext.classList.add('hidden');
            usernameediticon.src = 'public/static/media/img/check_24dp_FILL0_wght400_GRAD0_opsz24.svg';
            usernameinput.focus();
        } else {
            usernamediv.classList.remove('bg-color-mid', 'border-b-2', 'border-l-2', 'border-[#69D3C9]')
            usernameinput.classList.add('hidden');
            usernametext.classList.remove('hidden');
            usernameediticon.src = 'public/static/media/img/edit_24dp_FILL0_wght400_GRAD0_opsz24.svg';
        }

        content.name = usernameinput.value;
    }

    function editBio() {
        var biotext = document.getElementById('biotext');
        var bioinput = document.getElementById('bioinput');
        var bioediticon = document.getElementById('bioediticon');
        var biocharcount = document.getElementById('biocharcount');

        editingbio = !editingbio;

        if (editingbio == true) {
            bioinput.classList.remove('hidden');
            biocharcount.classList.remove('hidden');
            biotext.classList.add('hidden');
            bioediticon.src = 'public/static/media/img/check_24dp_FILL0_wght400_GRAD0_opsz24.svg';
            bioinput.focus();
        } else {
            bioinput.classList.add('hidden');
            biocharcount.classList.add('hidden');
            biotext.classList.remove('hidden');
            bioediticon.src = 'public/static/media/img/edit_24dp_FILL0_wght400_GRAD0_opsz24.svg';
        }

        biolength = bioinput.value.length;
        content.bio = bioinput.value;
    }

    function characterCount() {
        biolength = bioinput.value.length;
    }

</script>

<div class="bg-color-0">
    <!-- <p>{isUser}</p><p>{userID}</p> -->
    <Header />
    <div class="flex md:flex-row flex-col md:mx-24 bg-color-0 md:h-full rounded-2xl overflow-hidden mx-5 mb-10 mt-5">
        <div class="flex flex-col relative md:w-1/3 md:h-auto w-full space-y-7 pb-5">
            <img class="relative rounded-full w-2/3 aspect-square mx-auto shrink mt-8 ring-8 ring-[#69D3C9]" src="src/assets/img/profile picture placeholder.png" alt="">
            
            <div class="flex flex-row mx-auto space-x-3 rounded-lg" id="usernamediv">
                <input type="text" class="text-[150%] text-color-body w-full outline-none ps-2 pb-1 bg-color-mid hidden" value="{content.name}" id="usernameinput">
                <p class="text-2xl text-center text-color-body break-words" id="usernametext">{content.name}</p>
                {#if isUser}
                <button on:click={editName}>
                    <img src="public/static/media/img/edit_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="edit name" class="h-8" id="usernameediticon">
                </button>
                {/if}
            </div>
    
        </div>
    
        <div class="md:w-2/3 w-full">
            <div class="flex flex-row w-auto space-x-3">
                <p class="text-2xl mt-8 ms-10 text-color-title">Bio:</p>
                {#if isUser}
                <button on:click={editBio}>
                    <img src="public/static/media/img/edit_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="edit name" class="relative h-8 mt-8" id="bioediticon">
                </button>
                {/if}
            </div>
            <div class="md:mx-10 mx-2 mt-2 bg-color-mid rounded-2xl border-l-4 border-b-4 border-[#69D3C9]">
                <p class="p-5 text-justify text-color-body" id="biotext">{content.bio}</p>
                <textarea class="outline-none w-full resize-none p-5 text-color-body bg-color-mid hidden" on:input={characterCount} rows="10" maxlength="1500" id="bioinput">{content.bio}</textarea>
                <p class="relative text-right text-color-body pb-2 pe-3 hidden" id="biocharcount">{biolength}/1500</p>
            </div>
    
            <div class="md:mx-10 mx-2 mt-10 md:mb-16 mb-8">
                <p class="text-2xl text-color-title mb-4">Favorite Games</p>
                <div class="lg:columns-2 columns-1 space-y-5">
                    <FavoriteGames />
                    <FavoriteGames />
                    <FavoriteGames />
                    <FavoriteGames />
                </div>
            </div>
        </div>
    </div>

    <Footer />
</div>
