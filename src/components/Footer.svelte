<script>
  export let className = "";
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');

  .font-courier-prime {
      font-family: 'Courier Prime', monospace;
  }
</style>

<div class="flex flex-col bg-[#00141E] w-full h-[343px] {className} *:w-full *:*:mx-auto *:*:max-w-[1024px]">
  <div class="flex-1">
      <div class="container mx-auto mt-4 flex flex-col justify-between lg:flex-row">
          <div class="w-full lg:w-1/2">
              <div class="text-left">
                  <h2 class="text-lg font-bold text-blue-500 font-courier-prime">
                      <a href="#" class="text-blue-500 hover:underline">The Game Tips</a>
                  </h2>
                  <p class="text-white">Helping the gamers with their seek for tips</p>
                  <div class="mt-2 flex space-x-2">
                      <a href="#"><img src="/images/whatsapp-icon.SVG" alt="WhatsApp" class="h-6 w-6" /></a>
                      <a href="#"><img src="/images/twitter-icon.SVG" alt="Twitter" class="h-6 w-6" /></a>
                      <a href="#"><img src="/images/facebook-icon.SVG" alt="Facebook" class="h-6 w-6" /></a>
                  </div>
              </div>
          </div>

          <div class="mx-4 hidden flex-grow border-l border-gray-600 lg:block"></div>

          <div class="w-full lg:w-1/2">
              <div class="grid grid-cols-2 gap-8">
                  <div>
                      <h2 class="text-lg font-bold text-white">More Hints</h2>
                      <ul>
                          <li><a href="/minecraft" class="text-blue-500 hover:underline">Minecraft</a></li>
                          <li><a href="/survival-games" class="text-blue-500 hover:underline">Survival Games</a></li>
                          <li><a href="/horror" class="text-blue-500 hover:underline">Horror</a></li>
                          <li><a href="/elden-ring" class="text-blue-500 hover:underline">Elden Ring</a></li>
                          <li><a href="/genshin-impact" class="text-blue-500 hover:underline">Genshin Impact</a></li>
                          <li><a href="/red-dead-redemption-2" class="text-blue-500 hover:underline">Red Dead Redemption 2</a></li>
                      </ul>
                  </div>
                  <div>
                      <ul>
                          <br />
                          <li><a href="/roblox" class="text-blue-500 hover:underline">Roblox</a></li>
                          <li><a href="/playstation" class="text-blue-500 hover:underline">Playstation</a></li>
                          <li><a href="/multiversus" class="text-blue-500 hover:underline">Multiversus</a></li>
                          <li><a href="/plants-vs-zombies" class="text-blue-500 hover:underline">Plants vs Zombies</a></li>
                          <li><a href="/pokemon-black" class="text-blue-500 hover:underline">Pokemon Black</a></li>
                          <li><a href="/dragon-ball-kakarot" class="text-blue-500 hover:underline">Dragon Ball: Kakarot</a></li>
                      </ul>
                  </div>
              </div>
          </div>
      </div>
  </div>

  <div class="w-full h-[88px] bg-[#001B28] border-t-[5px] border-[#002331]">
      <div class="container mx-auto flex justify-center space-x-9">
          <div class="flex items-center space-x-20">
              <img src="logo.SVG" class="h-6 w-6" />
              <a href="/login" class="text-lg text-blue-500 hover:underline">Login</a>
          </div>
          <a href="/signin" class="text-lg text-blue-500 hover:underline">Sign in</a>
          <a href="/central" class="text-lg text-blue-500 hover:underline">Central</a>
          <a href="/help" class="text-lg text-blue-500 hover:underline">Help</a>
          <a href="/security-center" class="text-lg text-blue-500 hover:underline">Security Center</a>
          <a href="/community" class="text-lg text-blue-500 hover:underline">Community</a>
      </div>
  </div>
</div>
