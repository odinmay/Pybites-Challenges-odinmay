def generate_affiliation_link(url):
    """Split amazon urls into affiliate formatted urls"""

    base = 'http://www.amazon.com'
    _, mid, end = url.partition('/dp/')
    end = end.partition('/')[0]

    return base + mid + end + '/?tag=pyb0f-20'
