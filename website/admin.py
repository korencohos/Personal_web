from django.contrib import admin
from django.contrib import messages
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from .models import Section, ProjectItem, GalleryImage, About, SkillItem, FooterLink

# Use StackedInline instead of TabularInline
class ProjectItemInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ProjectItem
    extra = 1
    fields = ['title', 'description', 'image', 'link', 'pdf_file']

class GalleryImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = GalleryImage
    extra = 1

class SkillItemInline(SortableInlineAdminMixin, admin.StackedInline):
    model = SkillItem
    extra = 1

@admin.register(Section)
class SectionAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("title", "section_type", "order")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectItemInline]

    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        if obj:
            if obj.section_type == "projects":
                inline_instances.append(ProjectItemInline(self.model, self.admin_site))
            elif obj.section_type == "gallery":
                inline_instances.append(GalleryImageInline(self.model, self.admin_site))
            elif obj.section_type == "skills":
                inline_instances.append(SkillItemInline(self.model, self.admin_site))
        return inline_instances

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if add:
            messages.warning(
                request,
                mark_safe("💡 <strong>Tip:</strong> Save this section first to add related items like <em>projects</em>, <em>gallery images</em>, or <em>skills</em>.")
            )
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = ['image', 'content']
    pass

@admin.register(SkillItem)
class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'section', 'order')
    list_filter = ('section',)
    ordering = ('order',)

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
     list_display = ("label", "icon", "url", "order")
