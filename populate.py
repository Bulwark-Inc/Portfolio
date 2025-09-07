import os
import requests
import django
from django.utils.text import slugify
from django.core.files.base import ContentFile
from io import BytesIO


# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from home.models import DailyHeroText, Project, Service
from testimonials.models import Testimonial
from blogs.models import Blog, Category

# ----- DailyHeroText Entries -----
DAILY_ENTRIES = [
    {
        'header': 'Building Scalable Web Apps with Python & AI',
        'body': 'I’m Nonye Shiloh - a Fullstack Python Developer turning complex ideas into performant, AI-powered solutions.'
    },
    {
        'header': 'Data Science & AI: Turning Raw Data into Actionable Insights',
        'body': 'Discover how I leverage machine learning models to build intelligent systems and automate complex tasks.'
    },
    {
        'header': 'Secure & Robust Web Development',
        'body': 'From Django to Flask, I build secure, high-performance web applications that stand the test of time.'
    },
    {
        'header': 'Full-Stack Development: From Front to Back',
        'body': 'Learn about my expertise in crafting beautiful, responsive user interfaces and powerful back-end APIs.'
    },
    {
        'header': 'Leveraging Cloud Technologies for Scalability',
        'body': 'See how I deploy applications on platforms like AWS and Google Cloud to ensure your product scales with your business.'
    },
    {
        'header': 'API Design & Integration',
        'body': 'I specialize in creating and consuming RESTful and GraphQL APIs to connect your services seamlessly.'
    },
    {
        'header': 'Continuous Integration & Deployment (CI/CD)',
        'body': 'Explore how I automate development workflows to ensure fast, reliable, and frequent software releases.'
    },
]

# ----- Project Entries -----
PROJECT_ENTRIES = [
    {
        'title': 'MedInn',
        'description': 'A learning platform for medical students that leverages AI to personalize study materials, quiz generation, and revision planning — designed to help students pass with confidence.',
        'image': 'https://picsum.photos/seed/medinn/800/600',
        'github_link': '',
        'live_demo_link': 'https://medinn.shiloh.dev',
        'category': 'ai'
    },
    {
        'title': 'Nonware',
        'description': 'This personal portfolio site showcasing fullstack projects, services, and AI work — built using Django, Tailwind CSS, and deployed for high performance and accessibility.',
        'image': 'https://picsum.photos/seed/nonware/800/600',
        'github_link': 'https://github.com/nonye-shiloh/portfolio',
        'live_demo_link': 'https://nonye.shiloh.dev',
        'category': 'web'
    },
    {
        'title': 'Medacuit',
        'description': 'A SaaS platform designed for medical schools to conduct secure, large-scale exams with question banks, grading automation, and detailed performance analytics.',
        'image': 'https://picsum.photos/seed/medacuit/800/600',
        'github_link': '',
        'live_demo_link': 'https://medacuit.shiloh.dev',
        'category': 'web'
    },
    {
        'title': 'Healthy',
        'description': 'A lead generation and health guidance platform that collects health survey responses from expectant mothers and provides medically vetted tips — optimized for mobile onboarding.',
        'image': 'https://picsum.photos/seed/healthy/800/600',
        'github_link': '',
        'live_demo_link': 'https://healthy.shiloh.dev',
        'category': 'ai'
    }
]

# ----- Service Entries -----
SERVICE_ENTRIES = [
    {
        'title': 'Fullstack Web Development',
        'description': 'Crafting fast, secure, and scalable fullstack web applications using modern frameworks like Django, React, and Tailwind CSS — delivering seamless front-end and back-end integration.',
        'icon': 'globe',
        'link': 'https://nonye.shiloh.dev/fullstack-web'
    },
    {
        'title': 'Backend API Development',
        'description': 'Designing robust, RESTful and GraphQL APIs with Django REST Framework and FastAPI to power scalable, data-driven applications across web and mobile platforms.',
        'icon': 'server',
        'link': 'https://nonye.shiloh.dev/backend-api'
    },
    {
        'title': 'AI / Machine Learning',
        'description': 'Building intelligent systems using Python, scikit-learn, and TensorFlow — from data preprocessing to model deployment, with real-world applications in automation and analytics.',
        'icon': 'brain-cog',
        'link': 'https://nonye.shiloh.dev/ai-ml'
    },
    {
        'title': 'Mobile Development',
        'description': 'Creating high-performance, cross-platform mobile apps with Flutter and Dart, delivering smooth user experiences and native performance on both Android and iOS.',
        'icon': 'smartphone',
        'link': 'https://nonye.shiloh.dev/mobile'
    },
    {
        'title': 'Windows Development',
        'description': 'Building desktop applications for Windows using Python, PyQt, and Electron — ideal for internal tools, dashboards, and standalone software solutions.',
        'icon': 'monitor',
        'link': 'https://nonye.shiloh.dev/windows'
    },
    {
        'title': 'Updating Legacy Code',
        'description': 'Modernizing outdated systems by refactoring legacy codebases, introducing tests, improving security, and upgrading technologies to meet current performance and maintainability standards.',
        'icon': 'history',
        'link': 'https://nonye.shiloh.dev/legacy-code'
    }
]

TESTIMONIAL_ENTRIES = [
    {
        'name': 'Jane Doe',
        'designation': 'CTO, MedTech Inc.',
        'message': 'Working with Nonye was a game-changer. He transformed our legacy systems into scalable, AI-powered platforms — fast, clean, and incredibly efficient.',
        'photo': 'https://ui-avatars.com/api/?name=Jane+Doe&background=random&size=256',
        'is_approved': True
    },
    {
        'name': 'Chuka Okeke',
        'designation': 'Data Scientist & Mentor',
        'message': 'Nonye’s approach to data and AI is deeply insightful. His models aren’t just accurate — they’re production-ready and built to last.',
        'photo': 'https://randomuser.me/api/portraits/men/32.jpg',
        'is_approved': True
    },
    {
        'name': 'Amanda Zhang',
        'designation': 'Freelancer / UI Designer',
        'message': 'Every web project I collaborated on with Nonye ran smoother than I imagined. He has a knack for building stable, secure backends that just work.',
        'photo': 'https://randomuser.me/api/portraits/women/68.jpg',
        'is_approved': True
    },
    {
        'name': 'Tariq Al-Saleh',
        'designation': 'Startup Founder',
        'message': 'Fullstack developers like Nonye are rare. He handled our frontend, backend, and deployment pipelines with confidence and clarity.',
        'photo': 'https://randomuser.me/api/portraits/women/61.jpg',
        'is_approved': True
    },
    {
        'name': 'Ifunanya Eze',
        'designation': 'Cloud Engineer',
        'message': 'From AWS to GCP, Nonye knows how to scale infrastructure. His cloud strategy helped us handle traffic spikes with zero downtime.',
        'photo': 'https://randomuser.me/api/portraits/women/58.jpg',
        'is_approved': True
    },
    {
        'name': 'Lucien Dupont',
        'designation': 'API Consultant',
        'message': 'His API integrations were clean and well-documented. We barely needed to ask questions — everything just made sense.',
        'photo': 'https://randomuser.me/api/portraits/men/68.jpg',
        'is_approved': True
    },
    {
        'name': 'Miriam Ajayi',
        'designation': 'DevOps Specialist',
        'message': 'CI/CD was a mess until Nonye stepped in. He implemented seamless deployment pipelines that save us hours every week.',
        'photo': 'https://randomuser.me/api/portraits/women/18.jpg',
        'is_approved': True
    },
]

BLOG_ENTRIES = [
    {
        'title': 'How AI Is Revolutionizing Medical Education',
        'content': 'AI is transforming the way medical students learn by offering personalized content, adaptive quizzes, and real-time feedback. This post explores how platforms like MedInn are leading this change.',
        'image': 'https://picsum.photos/seed/ai-medical/800/600',
        'category_name': 'AI',
    },
    {
        'title': 'Building a Portfolio with Django and Tailwind CSS',
        'content': 'A step-by-step guide on creating a fast, responsive, and modern developer portfolio using Django as the backend and Tailwind CSS for styling.',
        'image': 'https://picsum.photos/seed/django-portfolio/800/600',
        'category_name': 'Web Development',
    },
    {
        'title': 'Launching a SaaS Platform for Medical Schools',
        'content': 'Medacuit is built to solve real challenges in medical school assessments. Here’s what went into building it, from infrastructure to UX decisions.',
        'image': 'https://picsum.photos/seed/saas-med/800/600',
        'category_name': 'SaaS',
    },
    {
        'title': 'Health Tech for Expectant Mothers: Lessons from Building Healthy',
        'content': 'Designing a health engagement tool for pregnant women meant balancing UX with clinical accuracy. This post breaks down the design, data, and impact.',
        'image': 'https://picsum.photos/seed/health-tech/800/600',
        'category_name': 'Health',
    },
]


# ----- Population Functions -----
def populate_daily_hero_text():
    print("Populating DailyHeroText...")
    DailyHeroText.objects.all().delete()
    for entry in DAILY_ENTRIES:
        DailyHeroText.objects.create(
            header=entry['header'],
            body=entry['body'],
            is_active=True
        )
        print(f"Created DailyHeroText: {entry['header']}")
    print("Done.\n")

def populate_projects():
    print("Populating Projects...")
    Project.objects.all().delete()
    for entry in PROJECT_ENTRIES:
        Project.objects.create(
            title=entry['title'],
            description=entry['description'],
            image=entry['image'],  # Ensure image path exists or use a placeholder
            github_link=entry['github_link'],
            live_demo_link=entry['live_demo_link'],
            category=entry['category']
        )
        print(f"Created Project: {entry['title']}")
    print("Done.\n")

def populate_services():
    print("Populating Services...")
    Service.objects.all().delete()
    for entry in SERVICE_ENTRIES:
        Service.objects.create(
            title=entry['title'],
            slug=slugify(entry['title']),
            description=entry['description'],
            icon=entry['icon'],
            link=entry['link']
        )
        print(f"Created Service: {entry['title']}")
    print("Done.\n")

def populate_testimonials():
    print("Populating Testimonials...")
    Testimonial.objects.all().delete()
    for entry in TESTIMONIAL_ENTRIES:
        Testimonial.objects.create(
            name=entry['name'],
            designation=entry['designation'],
            message=entry['message'],
            photo=entry['photo'],  # Ensure placeholder images exist or use blank if testing
            is_approved=entry['is_approved']
        )
        print(f"Created Testimonial: {entry['name']}")
    print("Done.\n")

def populate_blogs():
    print("Populating Blog Posts...")
    Blog.objects.all().delete()

    for entry in BLOG_ENTRIES:
        # Get or create category
        category, _ = Category.objects.get_or_create(name=entry['category_name'])

        # Download image if using external URL
        image_file = None
        if entry['image'].startswith('http'):
            response = requests.get(entry['image'])
            if response.status_code == 200:
                image_name = slugify(entry['title']) + '.jpg'
                image_file = ContentFile(response.content, name=image_name)

        blog = Blog.objects.create(
            title=entry['title'],
            content=entry['content'],
            image=image_file,  # will be None if download failed
            category=category
        )
        print(f"Created Blog: {blog.title}")

    print("Done.\n")

# ----- CLI Prompt -----
def run():
    print("Which model do you want to populate?")
    print("1. DailyHeroText")
    print("2. Projects")
    print("3. Services")
    print("4. Testimonials")
    print("5. Blogs")
    print("0. All")
    
    choice = input("Enter your choice (1/2/3/4/5/0): ").strip()

    if choice == '1':
        populate_daily_hero_text()
    elif choice == '2':
        populate_projects()
    elif choice == '3':
        populate_services()
    elif choice == '4':
        populate_testimonials()
    elif choice == '5':
        populate_blogs()
    elif choice == '0':
        populate_daily_hero_text()
        populate_projects()
        populate_services()
        populate_testimonials()
        populate_blogs()
    else:
        print("Invalid choice. Exiting.")

if __name__ == '__main__':
    run()
