// Design Token Template
// Customize these values based on your project's design style

export const tokens = {
  colors: {
    primary: '#1677FF',
    primaryHover: '#4096FF',
    primaryActive: '#0958D9',
    success: '#52C41A',
    warning: '#FAAD14',
    error: '#FF4D4F',
    info: '#1677FF',
    bgBase: '#FFFFFF',
    bgLayout: '#F5F5F5',
    bgElevated: '#FFFFFF',
    bgContainer: '#FFFFFF',
    textPrimary: '#1F1F1F',
    textSecondary: '#8C8C8C',
    textTertiary: '#BFBFBF',
    textDisabled: '#D9D9D9',
    borderBase: '#D9D9D9',
    borderLight: '#F0F0F0',
  },
  typography: {
    fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    fontSize: {
      xs: '12px', sm: '13px', base: '14px', lg: '16px',
      xl: '20px', '2xl': '24px', '3xl': '30px',
    },
    fontWeight: {
      normal: 400, medium: 500, semibold: 600, bold: 700,
    },
    lineHeight: {
      tight: 1.25, base: 1.5, relaxed: 1.75,
    },
  },
  spacing: {
    unit: '8px', xs: '4px', sm: '8px', md: '16px',
    lg: '24px', xl: '32px', '2xl': '48px',
    pagePadding: '24px', sectionGap: '32px',
  },
  borderRadius: {
    none: '0', sm: '4px', base: '8px', lg: '12px', full: '9999px',
  },
  shadows: {
    none: 'none',
    sm: '0 1px 2px rgba(0,0,0,0.05)',
    base: '0 1px 3px rgba(0,0,0,0.1)',
    md: '0 4px 12px rgba(0,0,0,0.08)',
    lg: '0 8px 24px rgba(0,0,0,0.12)',
  },
  breakpoints: {
    sm: '640px', md: '768px', lg: '1024px', xl: '1280px', '2xl': '1536px',
  },
  transitions: {
    fast: '150ms ease', base: '200ms ease', slow: '300ms ease',
  },
} as const;

export type Tokens = typeof tokens;
