
<script>
    import Header from ".././components/Header.svelte";
    import Footer from ".././components/Footer.svelte";
  
    
  let nickname = '';
  let email = '';
  let password = '';
  let confirmPassword = '';

  function handleFormSubmit() {
    console.log('Formulário enviado!');
  };
  
    let routes = [
      ["/#/login", "Login"],
      ["/#/sigin", "Sign In"],
      ["/#/about", "About Us"],
      ["/#/help", "Help"],
      ["https://github.com/rakRandom/dicas-de-jogos-site", "Community"],
    ];
  </script>
  
  <style>
    /* TailwindCSS Utility Classes */
    .header-bg {
      background-color: #00141e;
      width: 100%;
      max-width: 500px;
      margin: auto;
      margin-top: 20px;
    }
  
    .form-bg {
      background-color: #002331;
      background-image: url('backin.jpg');
      background-size: cover;
      background-position: center;
      margin-top: 1rem;
      margin-bottom: 3rem; 
      max-width: 500px;
      margin: auto;
      padding: 2rem; 
    }
  
    .title-color {
      color: #2ec4b6;
      font-family: 'Roboto';
    }
  
    .button-bg {
      background-color: #051d26;
      border: 2px solid #2ec4b6;
      padding: 0.75rem 0;
      width: 100%;
      max-width: 300px;
      margin: auto;
      transition: transform 0.3s ease, background-color 0.3s ease;
    }
  
    .button-bg:hover {
      transform: scale(1.05);
      background-color: #2ec4b6;
    }
  
    .button-bg1 {
      background-color: #2ec4b6;
      border: 2px solid #2ec4b6;
      padding: 0.75rem 0;
      width: 100%;
      max-width: 300px;
      margin: auto;
      transition: transform 0.3s ease, background-color 0.3s ease;
    }
  
    .button-bg1:hover {
      transform: scale(1.05);
      background-color: #051d26;
    }
  
    .text-input-bg {
      background-color: #051d26;
      border-bottom: 2px solid #2ec4b6;
      padding: 0.5rem;
    }
  
    .text-input-bg:hover {
      border-bottom: 3px solid #2ec4b6;
    }
  
    .centered-form {
      max-width: 500px;
      margin: auto;
    }
  
    .underline {
      text-decoration: underline;
    }
  
    .or-text {
      color: white;
    }
  
    .or-line {
      border-top: 3px solid #2ec4b6;
      width: 150px;
    }
  </style>
  <Header />
  <div class="w-full h-auto">
    <img src="/backgroundImage.svg" alt="">
  <div class="header-bg flex items-center justify-center p-2 ">
    <img src="logoImage.svg" alt="Logo" class="mr-2 w-16 h-16" />
    <h1 class="title-color text-xl">The Game Tips</h1>
  </div>
  
  <div class="form-bg centered-form p-4">
    <div class="mb-4 text-center">
      <span class="title-color">Already have an account?</span>
      <a href="/signin" class="title-color font-bold underline">Sign in</a>
    </div>
    <div class="mb-3">
      <label for="nickname" class="title-color">Nickname</label>
      <input type="text" id="nickname" value="{nickname}" class="text-input-bg text-input-line w-full" placeholder="Choose a nickname" />
    </div>
    <div class="mb-3">
      <label for="email" class="title-color">Email</label>
      <input type="email" id="email" value="{email}" class="text-input-bg text-input-line w-full" placeholder="Enter your email" />
    </div>
    <div class="mb-3">
      <label for="password" class="title-color">Password</label>
      <input type="password" id="password" value="{password}" class="text-input-bg text-input-line w-full" placeholder="Create a password" />
    </div>
    <div class="mb-7">
      <label for="confirm-password" class="title-color">Confirm Password</label>
      <input type="password" id="confirm-password" class="text-input-bg text-input-line w-full" placeholder="Confirm your password" />
    </div>
    <button class="button-bg1 flex w-full items-center justify-center text-white">Create Account</button>
  
    <div class="my-4 flex items-center justify-center">
      <div class="or-line mr-5"></div>
      <span class="or-text">or</span>
      <div class="or-line ml-5"></div>
    </div>
  
    <!-- Botões de Continue with Google e Facebook com imagens -->
    <button class="button-bg flex w-full items-center justify-center text-white">
      <img src="../src/assets/img/googleImage.svg" alt="Google" class="mr-2 w-10 h-10" />
      Continue with Google
    </button>
    <button class="button-bg mt-2 flex w-full items-center justify-center text-white">
      <img src="../src/assets/img/icons8-facebook-novo.svg" alt="Facebook" class="mr-2 w-8 h-8" />
      Continue with Facebook
    </button>
  </div>
</div>
  <br>
  <Footer />
  