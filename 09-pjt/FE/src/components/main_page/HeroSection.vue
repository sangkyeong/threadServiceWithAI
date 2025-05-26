<template>
<!-- 2. Hero 섹션 -->
<section class="hero-section">
    <img src="@/assets/hero_image.jpg" alt="Hero Image" class="hero-img" />
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <!-- 1. 가운데 문구 -->
        <!-- <h1 class="hero-title">AI 기반 도서 추천 커뮤니티 서비스</h1> -->
        
        <!-- 2. 가운데 문구 -->
        <h1 class="hero-title">책과 함께하는 하루</h1>
        <p class="hero-title">지금, 당신의 인생책을 만나보세요.</p>

    <div class="hero-subtitle">
        <span>Th</span><span style="color: #fe4a51">Read</span>
    </div>
    </div>
</section>

</template>

<script setup>

</script>

<style scoped>

@font-face {
    font-family: "SBAggro_L";
    src: url("https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/SBAggroL.woff")
        format("woff");
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: "GmarketSansMedium";
    src: url("https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff")
        format("woff");
    font-weight: normal;
    font-style: normal;
}

/* Navbar 관련 스타일 */
/* 로고 font 설정 */
a.navbar-brand {
    font-family: "GmarketSansMedium";
}
/* 메뉴 폰트 설정 */
.menu-item {
    font-family: "SBAggro_L";
}

/* Hero 섹션 관련 스타일 */
.hero-section {
    background: url('/images/hero-bg.jpg');
    min-height: 80vh;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #fff;
}

.hero-section img.hero-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
}

.hero-overlay {
    background: rgba(0, 0, 0, 0.5);
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 3;
}

.hero-title {
    font-family: "GmarketSansTTFMedium";
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    border-radius: 0.2rem;
    padding: 0 1rem;
}

.hero-subtitle {
    font-weight: 700;
    font-size: 1.5rem;
}

</style>