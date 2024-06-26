<script>
  import Header from "../components/Header.svelte";
  import Footer from "../components/Footer.svelte";

  let src = "../public/backgroundImageRegister.svg";
  
  let nickname = '';
  let email = '';
  let password = '';
  let confirmPassword = '';

  function handleFormSubmit() {
      console.log('Formulário enviado!');
  };

  let routes = [
      ["/#/login", "Login"],
      ["/#/signup", "Sign Up"],
      ["/#/about", "About Us"],
      ["/#/help", "Help"],
      ["https://github.com/rakRandom/dicas-de-jogos-site", "Community"],
  ];
</script>

<style>
.form-bg {
  background-image: url({src});
}
</style>

<Header />

<div class="w-full max-w-[500px] mx-auto mt-[140px] rounded-lg overflow-hidden shadow-lg">
<div class="bg-[#00141e] flex items-center justify-center p-2">
  <img src="../../public/logoImage.svg" alt="" class="mr-2" />
  <h1 class="text-[#2ec4b6] font-[Courier Prime] text-xl">The Game Tips</h1>
</div>
<div class="form-bg bg-[#002331] bg-cover bg-center p-8 flex flex-col items-center">
  <div class="mb-4 text-center">
    <span class="text-[#2ec4b6]">Already have an account?</span>
    <a href="/signin" class="text-[#2ec4b6] font-bold underline">Sign in</a>
  </div>
  <div class="mb-3 w-full">
    <label for="nickname" class="text-[#2ec4b6]">Nickname</label>
    <input type="text" id="nickname" class="bg-[#051d26] border-b-2 border-[#2ec4b6] p-2 w-full rounded-t-md text-white outline-none" placeholder="Choose a nickname" />
  </div>
  <div class="mb-3 w-full">
    <label for="email" class="text-[#2ec4b6]">Email</label>
    <input type="email" id="email" class="bg-[#051d26] border-b-2 border-[#2ec4b6] p-2 w-full rounded-t-md text-white outline-none" placeholder="Enter your email" />
  </div>
  <div class="mb-3 w-full">
    <label for="password" class="text-[#2ec4b6]">Password</label>
    <input type="password" id="password" class="bg-[#051d26] border-b-2 border-[#2ec4b6] p-2 w-full rounded-t-md text-white outline-none" placeholder="Create a password" />
  </div>
  <div class="mb-7 w-full">
    <label for="confirm-password" class="text-[#2ec4b6]">Confirm Password</label>
    <input type="password" id="confirm-password" class="bg-[#051d26] border-b-2 border-[#2ec4b6] p-2 w-full rounded-t-md text-white outline-none" placeholder="Confirm your password" />
  </div>
  <button class="bg-[#051d26] border-2 border-[#2ec4b6]  py-3 w-full max-w-[200px] transition-transform transform hover:scale-105 hover:bg-[#2ec4b6] text-white rounded-2xl">Create Account</button>

  <div class="my-4 flex items-center justify-center w-full">
    <div class="border-t-2 border-[#2ec4b6] w-[30%]"></div>
    <span class="text-white mx-4">or</span>
    <div class="border-t-2 border-[#2ec4b6] w-[30%]"></div>
  </div>

  <button class="bg-[#051d26] border-2 border-[#2ec4b6] py-3 w-full flex justify-center items-center text-white transition-transform transform hover:scale-105 hover:bg-[#2ec4b6] rounded-md">
    <img src="google.svg" alt="Google" class="mr-2" />
    Continue with Google
  </button>
  <button class="bg-[#051d26] border-2 border-[#2ec4b6] py-3 mt-2 w-full flex justify-center items-center text-white transition-transform transform hover:scale-105 hover:bg-[#2ec4b6] rounded-md">
    <img src="facebook.svg" alt="Facebook" class="mr-2" />
    Continue with Facebook
  </button>
</div>
</div>

<Footer/>
