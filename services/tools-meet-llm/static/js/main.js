const observer = new IntersectionObserver(
  entries => {
    let topmostElement = null
    let topmostEntry = null

    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // 目标元素进入页面
        // 这里可以执行您的逻辑处理
        if (!topmostElement || entry.boundingClientRect.top < topmostEntry.boundingClientRect.top) {
          topmostElement = entry.target
          topmostEntry = entry
        }
      }
    })

    if (topmostElement) {
      // 最靠上的元素
      console.log('最靠上的元素:', topmostElement.id)
      handleActive(topmostElement.id)
      // 这里可以执行您的逻辑处理
    }
  },
  {
    root: null,
    threshold: 0.3
  }
)

function setClickEventListener(elements) {
  for (let index = 0; index < elements.length; index++) {
    const element = elements[index]
    console.log('element', element)
    element.addEventListener('click', () => {
      console.log('点击了 ', element, element.href.split('#')[1])
      element.classList.add('active')
      handleActive(element.href.split('#')[1])
    })
  }
}

function handleActive(id) {
  var elements = document.getElementsByClassName('llm-nav-item')
  for (let index = 0; index < elements.length; index++) {
    const element = elements[index]
    if (elements[index].href.split('#')[1] !== id) {
      element.classList.remove('active')
    } else {
      element.classList.add('active')
    }
  }
}

setClickEventListener(document.getElementsByClassName('llm-nav-item'))

function setSectionObserver(elements) {
  for (let index = 0; index < elements.length; index++) {
    observer.observe(elements[index])
  }
}
setSectionObserver(document.getElementsByClassName('section'))
