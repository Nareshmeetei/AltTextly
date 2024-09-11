<template>
    <div>
      <a :href="backgroundLink" class="background-link" id="backgroundLink" target="_blank" rel="noopener noreferrer">
        <!-- This is an empty anchor that covers the entire background -->
      </a>
      <header>
        <a href="/" class="logo">
          <img :src="~/assets/images/alttextly-logo-black.svg" alt="AltTextly Logo">
        </a>
        <div class="nav-container-wrapper">
          <div class="nav-container">
            <button v-for="item in navItems" :key="item" class="nav-button">{{ item }}</button>
          </div>
          <button class="nav-button dark">Unlock All Features</button>
        </div>
      </header>
      <main>
        <section class="left-panel">
          <h1>Generate Alt Text. Free and Fast.</h1>
          <div class="file-input">
            <div class="file-input-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 5V19M5 12H19" stroke="#e8e8e8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="file-input-text">
              <span>Add files</span>
              <span class="file-input-subtext">Or select a folder</span>
            </div>
          </div>
          <button class="create-button">Create Alt Text</button>
          <div class="google-signup">
            <svg class="google-logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
              <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/>
              <path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/>
              <path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/>
              <path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"/>
            </svg>
            Sign up with Google
          </div>
          <p class="get-pro">Get Pro - Unlock All Features</p>
        </section>
      </main>
      <footer>
        <p>Copyright © {{ currentYear }} AltText™</p>
        <nav>
          <a v-for="link in footerLinks" :key="link.text" :href="link.href">{{ link.text }}</a>
        </nav>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        backgroundLink: 'https://unsplash.com/photos/a-close-up-of-a-cell-phone-with-a-purple-background-aQVeOg9SiE8',
        logoSrc: '/images/alttextly-logo-black.svg',
        navItems: ['Features', 'Resources', 'Blog', 'Sign In'],
        currentYear: new Date().getFullYear(),
        footerLinks: [
          { text: 'Promote your brand/product', href: '#' },
          { text: 'Terms of Service', href: '#' },
          { text: 'Privacy Policy', href: '#' }
        ]
      }
    },
    methods: {
      handleLogoError(e) {
        e.target.src = '/images/alttextly logo black.png';
        console.log('SVG failed to load, trying PNG');
      },
      updateBackgroundImage(imagePath) {
        document.body.style.backgroundImage = `url('${imagePath}')`;
        this.backgroundLink = imagePath;
        this.checkBackgroundBrightness();
      },
      checkBackgroundBrightness() {
        // Implement the logic to check background brightness
      }
    },
    mounted() {
      // Set the background image
      document.body.style.backgroundImage = `url('https://images.unsplash.com/photo-1676293963736-260e3b78e643?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')`;
    }
  }
  </script>
  
  <style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  html, body {
    height: 100%;
  }
  .background-link {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    cursor: pointer;
  }
  body {
    font-family: 'Geist', sans-serif;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: -1;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: 'Geist', sans-serif;
    font-weight: 700;
  }
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    width: 100%;
    position: absolute;
    top: 0;
  }
  .logo {
    display: flex;
    align-items: center;
    font-weight: bold;
    font-size: 1.2rem;
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.1))
            drop-shadow(0 0 5px rgba(255, 255, 255, 0.3))
            drop-shadow(0 0 5px rgba(255, 255, 255, 0.3));
  }
  .logo-icon {
    width: 30px;
    height: 30px;
    background-color: #333;
    border-radius: 50%;
    margin-right: 0.5rem;
  }
  .nav-container-wrapper {
    display: flex;
    align-items: center;
  }
  .nav-container {
    display: flex;
    gap: 1rem;
    background-color: rgba(246, 246, 246, 0.8);
    padding: 0.5rem 1rem;
    border-radius: 100px;
    height: 48px;
    align-items: center;
  }
  .nav-button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 100px;
    background-color: transparent;
    cursor: pointer;
    height: 100%;
    display: flex;
    align-items: center;
  }
  .nav-button.dark {
    background-color: #333;
    color: rgb(246, 246, 246);
    margin-left: 1rem;
    height: 48px;
    width: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  main {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    height: 100%;
    padding: 2rem;
    padding-left: 8%;
  }
  .left-panel {
    background-color: rgb(246, 246, 246);
    padding: 2rem;
    border-radius: 40px;
    box-shadow: 0 4px 6px rgba(185, 185, 185, 0.1);
    max-width: 300px;
    width: 100%;
    text-align: center;
    border: 1px solid #dedede;
  }
  h1 {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    text-align: left;
  }
  .file-input {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border: 2px solid #ccc;
    border-radius: 100px;
    cursor: pointer;
    margin-bottom: 1rem;
  }
  .file-input-icon {
    width: 32px;
    height: 32px;
    background-color: #333;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .file-input-icon svg {
    width: 16px;
    height: 16px;
  }
  .file-input-text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  .file-input-subtext {
    color: #B3B3B3;
    font-size: 0.8em;
  }
  .create-button {
    width: 100%;
    height: 48px;
    font-size: .9em;
    font-weight: 550;
    color: #e8e8e8;
    padding: 0.5rem;
    background-color: #a5a5a5;
    border: none;
    border-radius: 100px;
    cursor: pointer;
    margin-bottom: 5rem;
  }
  .google-signup {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8em;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border: 1px solid #ccc;
    border-radius: 100px;
    cursor: pointer;
    margin-bottom: 1rem;
  }
  .google-logo {
    width: 20px;
    height: 20px;
  }
  .get-pro {
    font-weight: 600;
    font-size: 1em;
    text-decoration: underline;
  }
  footer {
    display: flex;
    justify-content: space-between;
    padding: 0.2rem 2rem;
    background-color: rgba(255, 255, 255, 0.5);
    opacity: 1;
    width: 100%;
    position: absolute;
    bottom: 0;
    font-size: 0.7rem;
    font-weight: 300;
  }
  footer nav {
    display: flex;
    gap: 1rem;
  }
  footer p {
    color: rgb(40, 40, 40);
  }
  footer a {
    color: rgb(40, 40, 40);
    text-decoration: none;
  }
  footer a:hover {
    text-decoration: underline;
  }
  </style>